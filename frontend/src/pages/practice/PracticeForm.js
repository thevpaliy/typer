import React from "react";
import { connect } from "react-redux";
import { actions } from "@actions";
import styled from "styled-components";
import Dictionary from "./DictionarySection";
import TypedSection from "./TypedSection";

const InputBox = styled.div`
  -webkit-user-modify: read-write;
  -moz-user-modify: read-write;
  user-modify: read-write;
  display: inline-block;
  border: none;
  outline: none;
  font-size: 56px;
  text-align: right;
  line-height: 56px;
  white-space: nowrap;
  min-height: 56px;
  color: ${props => (props.valid ? "#4892dc" : "palevioletred")};
  text-decoration: ${props => (props.valid ? "none" : "line-through")};
  text-decoration-style: solid;
  text-decoration-color: palevioletred;
  padding-left: 1rem;
`;

const Wrapper = styled.div`
  display: flex;
  align-items: center;
`;

const Playground = styled.div`
  display: flex;
  align-items: center;
  background-color: #fafafa;
  width: 100%;
  height: 200px;
  * > {
    width: 100%;
    height: 100%;
  }
`;

class PracticeForm extends React.Component {
  state = {
    session: {
      correct: 0,
      wrong: 0,
      chars: 0
    },
    typed: [],
    valid: true
  };

  dictionaryRef = React.createRef();
  inputBoxRef = React.createRef();

  onTyped = event => {
    let dictionary = this.dictionaryRef.current;
    let inputBox = this.inputBoxRef.current;
    let { typed, session, valid } = this.state;
    let current = inputBox.innerHTML;

    switch (event.keyCode) {
      // space key code
      case 32:
        event.preventDefault();
        typed.push({
          intended: dictionary.getCurrent(),
          typed: current
        });
        inputBox.innerHTML = null;
        dictionary.shiftToNext();
        valid = true;
        break;
      case 8:
        current = current.slice(0, -1);
        dictionary.trimCurrent(current);
        break;
      default:
        if (event.key.length == 1) {
          current += event.key;
          dictionary.trimCurrent(current);
        }
        valid = dictionary.startsWith(current);
    }
    this.setState({
      typed,
      session,
      valid
    });
  };

  render() {
    return (
      <Wrapper>
        <Playground>
          <TypedSection typed={this.state.typed} />
          <InputBox
            valid={this.state.valid}
            ref={this.inputBoxRef}
            contentEditable={true}
            spellCheck={false}
            autoCorrect="off"
            autoComplete="off"
            onKeyDown={this.onTyped}
          />
          <Dictionary ref={this.dictionaryRef} />
        </Playground>
      </Wrapper>
    );
  }
}

const mapStateToProps = state => ({});

const mapDispatchToProps = dispatch => ({
  fetchWords: () => dispatch({}),
  submit: session => dispatch({})
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(PracticeForm);
