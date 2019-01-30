import React from "react";
import styled from "styled-components";

const Wrapper = styled.div`
  display: flex;
  flex: 1;
`;

const DigitInput = styled.input`
  width: 3rem;
  height: 3rem;
  border-radius: 4px;
  border-width: 0.75px;
  background-color: transparent;
  text-align: center;
  font-size: 26px;
  padding: 0;
  margin-left: 1rem;
  margin-right: 1rem;
`;

class Confirmation extends React.Component {
  inputRefs = [];
  constructor(props) {
    super(props);
    this.state = {
      inputs: new Array(this.props.count),
      index: 0
    };
  }

  onChange = event => {
    const { value } = event.target;
    if (!value) {
      return;
    }

    const { onFinished, count } = this.props;
    const { inputs, index } = this.state;

    if (count > index + 1) {
      this._setFocus(index + 1);
    } else if (onFinished) {
      const current = inputs.reduce((x, y) => x + y, new String());
      onFinished(current);
    }

    this.setState(state => ({
      inputs: inputs,
      index: state.index + 1
    }));
  };

  _setFocus = index => {
    this.inputRefs[index].focus();
  };

  onFocused = index => {
    let inputs = this.state.inputs;
    const currentEmptyIndex = inputs.findIndex(e => !e);
    if (currentEmptyIndex !== -1 && currentEmptyIndex < index) {
      //this._setFocus(currentEmptyIndex);
      return
    }
    for (const i in inputs) {
      if (i >= index) {
        inputs[i] = null;
      }
    }

    this.setState({
      inputs: inputs,
      index: index
    });
  };

  onKeyDown = event => {
    if (event.nativeEvent.key === "Backspace") {
      const { index } = this.state;
      const nextIndex = index > 0 ? index - 1 : 0;
      this._setFocus(nextIndex);
      this.setState({
        index: nextIndex
      });
    }
  };

  render() {
    const { inputs, index } = this.state;
    const { count } = this.props;
    return (
      <Wrapper>
        {Array.from({ length: count }, (x, i) => i).map(key => (
          <DigitInput
            key={key}
            value={inputs[key]}
            maxLength={1}
            autoFocus={index == key}
            ref={ref => (this.inputRefs[key] = ref)}
            onChange={this.onChange}
            onKeyDown={this.onKeyDown}
            onFocus={() => this.onFocused(key)}
          />
        ))}
      </Wrapper>
    );
  }
}

export default Confirmation;
