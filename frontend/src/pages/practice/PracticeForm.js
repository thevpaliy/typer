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

class PracticeForm extends React.Component {
  onTyped = event => {};

  render() {
    return (
      <Wrapper>
        <Playground>
          <InputBox
            contentEditable={true}
            spellCheck={true}
            autoCorrect="off"
            autoComplete="off"
          />
          <Dictionary />
        </Playground>
      </Wrapper>
    );
  }
}

export default PracticeForm;
