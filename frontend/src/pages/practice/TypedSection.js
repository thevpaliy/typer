import React from "react";
import styled from "styled-components";

const Wrapper = styled.div`
  overflow: hidden;
  display: flex;
  align-items: center;
  flex-grow: 5;
  > *:first-child {
    padding-left: 0px;
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

class TypedSection extends React.Component {
  state = {
    index: 0,
    current: null,
    typed: []
  };

  render() {
    let { current, index, typed } = this.state;
    typed = [current ? current.slice(index) : null]
      .concat(typed)
      .filter(w => w)
      .map(w => w.trim());
    return (
      <Wrapper>
        {typed.map(word => (
          <Word>{word}</Word>
        ))}
      </Wrapper>
    );
  }
}

export default TypedSection;
