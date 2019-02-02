import React from "react";
import styled from "styled-components";

const MetricTitle = styled.span`
  text-transform: uppercase;
  font-size: 12px;
  font-weight: lighter;
`;

const WordsWrapper = styled.div`
  overflow: hidden;
  display: flex;
  align-items: center;
  flex-grow: 5;
  > span:first-child {
    padding-left: 0px;
  }

  > span {
    font-size: 56px;
    padding-right: 10px;
    padding-left: 10px;
    line-height: 56px;
    text-align: left;
    margin: 0;
  }
`;

const TypedWrapped = styled.div`
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  text-align: right;
  color: #4892dc;
  > span:first-child {
    padding-left: 0px;
  }

  > span {
    font-size: 56px;
    padding-right: 10px;
    padding-left: 10px;
    line-height: 56px;
    text-align: left;
    margin: 0;
  }
`;

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
  background-color: white;
  height: 200px;
  * > {
    width: 100%;
    height: 100%;
  }
`;
