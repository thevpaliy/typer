import React from "react";
import styled from "styled-components";

const Wrapper = styled.div`
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  text-align: right;
  color: #4892dc;
  > span {
    padding-right: 1rem;
  }
`;

const Word = styled.span`
  font-size: 30.4px;
  line-height: 30.4px;
  text-align: left;
`;

const MistypedWord = styled.span`
  font-size: 30.4px;
  line-height: 30.4px;
  text-align: left;
  color:palevioletred
  text-decoration: line-through;
  text-decoration-style: solid;
  text-decoration-color: palevioletred;
`;

const createWord = (intended, typed) =>
  intended == typed ? (
    <Word> {typed} </Word>
  ) : (
    <MistypedWord> {typed} </MistypedWord>
  );

const TypedSection = ({ typed }) => (
  <Wrapper>
    {" "}
    {typed.map(input => createWord(input.intended, input.typed))}{" "}
  </Wrapper>
);

export default TypedSection;
