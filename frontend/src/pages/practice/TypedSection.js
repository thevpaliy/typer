import React from "react";
import styled from "styled-components";

const Wrapper = styled.div`
  overflow: hidden;
  display: flex;
  align-items: center;
  flex-grow: 1;
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
  intended == typed ? (
    <Word>{typed}</Word>
  ) : (
    <MistypedWord>{typed}</MistypedWord>
  );

const TypedSection = ({ typed }) => (
  <Wrapper>
    {typed.map(input => createWord(input.intended, input.typed))}
  </Wrapper>
);

export default TypedSection;
