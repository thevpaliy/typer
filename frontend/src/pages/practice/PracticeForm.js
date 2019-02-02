import React from "react";
import styled from "styled-components";
import Dictionary from "./DictionarySection";
import Typed from "./TypedSection";

const InputBox = styled.div`
  -webkit-user-modify: read-write;
  -moz-user-modify: read-write;
  user-modify: read-write;
  display: inline-block;
  padding-left: 5px;
  border: none;
  outline: none;
  font-size: 56px;
  color: #4892dc;
  text-align: right;
  line-height: 56px;
  white-space: nowrap;
  min-height: 56px;
  text-decoration-color: #4892dc;
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

const Word = styled.span`
  font-size: 56px;
  padding-right: 10px;
  padding-left: 10px;
  line-height: 56px;
  text-align: left;
  margin: 0;
`;

const MistypedWord = styled.span`
  font-size: 56px;
  padding-right: 10px;
  padding-left: 10px;
  line-height: 56px;
  text-align: left;
  margin: 0;
`;

const createWord = (intended, typed) =>
  intended.startsWith(typed) ? (
    <Word>{typed}</Word>
  ) : (
    <MistypedWord>{typed}</MistypedWord>
  );

class PracticeForm extends React.Component {
  dictionaryRef = React.createRef();

  onTyped = event => {
    switch (event.keyCode) {
      // space key code
      case 32:
        console.log("handing space")
        event.preventDefault()
        break
      // backspace key code
      case 8:
        console.log("handing backspace")
        break;
      // any other key
      default:
        console.log("handling a key here")
    }
  };

  render() {
    return (
      <Wrapper>
        <Playground>
          <InputBox
            contentEditable={true}
            spellCheck={true}
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

export default PracticeForm;
