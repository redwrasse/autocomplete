import React, {Component} from 'react';
import PropTypes from 'prop-types';
import './App.css';

const App = () => {
    return (
        <div className="App">
            <Autocomplete
                options={[
                    // "Apple",
                    // "Papaya",
                    // "Persimmon",
                    // "Paw Paw",
                    // "Prickly Pear",
                    // "Peach",
                    // "Pomegranate",
                    // "Pineapple"
                ]}
            />
        </div>
    );
};

class Autocomplete extends Component {
    static propTypes = {
        options: PropTypes.instanceOf(Array).isRequired
    };
    state = {
        activeOption: 0,
        filteredOptions: [],
        showOptions: false,
        userInput: ''
    };


    runSearch(userInput) {
        const requestOptions = {
            method: 'post',
            mode: 'cors',
            credentials: 'same-origin',
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ userInput: userInput })
        };
        fetch('http://localhost:5000/search', requestOptions)
            .then(response => response.json())
            .then(data => {
                // clear existing
                this.setState({filteredOptions: []});
                let matches = data.matches;
                for (var i = 0; i < matches.length; i++) {
                    this.setState({ filteredOptions: [...this.state.filteredOptions, matches[i]] })
                }
            })
            .catch((err)=>console.log(err));
    }

    onChange = (e) => {

        const { options } = this.props;
        const userInput = e.currentTarget.value;

        this.runSearch(userInput);


        this.setState({
            activeOption: 0,
            //filteredOptions,
            showOptions: true,
            userInput: e.currentTarget.value
        });
    };

    onClick = (e) => {
        console.log('clicked');
        this.setState({
            activeOption: 0,
            filteredOptions: [],
            showOptions: false,
            userInput: e.currentTarget.innerText
        });
    };
    onKeyDown = (e) => {
        const { activeOption, filteredOptions } = this.state;

        if (e.keyCode === 13) {
            this.setState({
                activeOption: 0,
                showOptions: false,
                userInput: filteredOptions[activeOption]
            });
        } else if (e.keyCode === 38) {
            if (activeOption === 0) {
                return;
            }
            this.setState({ activeOption: activeOption - 1 });
        } else if (e.keyCode === 40) {
            if (activeOption === filteredOptions.length - 1) {
                console.log(activeOption);
                return;
            }
            this.setState({ activeOption: activeOption + 1 });
        }
    };

    render() {
        const {
            onChange,
            onClick,
            onKeyDown,

            state: { activeOption, filteredOptions, showOptions, userInput }
        } = this;
        let optionList;
        if (showOptions && userInput) {
            if (filteredOptions.length) {
                optionList = (
                    <ul className="options">
                        {filteredOptions.map((optionName, index) => {
                            let className;
                            if (index === activeOption) {
                                className = 'option-active';
                            }
                            return (
                                <li className={className} key={optionName} onClick={onClick}>
                                    {optionName}
                                </li>
                            );
                        })}
                    </ul>
                );
            } else {
                optionList = (
                    <div className="no-options">
                        <em>No Option!</em>
                    </div>
                );
            }
        }
        return (
            <React.Fragment>
                <div className="search">
                    <input
                        type="text"
                        className="search-box"
                        onChange={onChange}
                        onKeyDown={onKeyDown}
                        value={userInput}
                    />
                    <input type="submit" value="" className="search-btn" />
                </div>
                {optionList}
            </React.Fragment>
        );
    }
}


export default App;
