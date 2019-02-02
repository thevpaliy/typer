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

class Dictionary extends React.Component {
  constructor(props) {
    super(props);
    this.state = this._buildState(props.words);
  }

  _buildState(words) {
    words = words || [];
    return {
      index: 0,
      current: words.length ? words[0] : null,
      words: words.length ? words.slice(1) : []
    };
  }

  populateWith(words) {
    this.setState(this._buildState(words));
  }

  shiftToNext() {
    const { words } = this.state;
    this.setState(this._buildState(words.slice(-1)));
  }

  trimCurrent(word) {
    const current = this.state.current;
    if (current == word) {
      this.shiftToNext();
      return;
    }
    let index = 0;
    for (let char of word) {
      if (current[index] != char) {
        break;
      }
      index++;
    }
    this.setState({ index });
  }

  startsWith(word) {
    const current = this.state.current;
    return current && current.startsWith(word);
  }

  render() {
    let { current, index, words } = this.state;
    words = [current ? current.slice(index) : null]
      .concat(words)
      .filter(w => w)
      .map(w => w.trim());
    return (
      <Wrapper>
        {words.map(word => (
          <Word>{word}</Word>
        ))}
      </Wrapper>
    );
  }
}

export default Dictionary;