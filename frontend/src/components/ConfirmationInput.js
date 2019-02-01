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
  border-style: solid;
  border-color: #e0e0e0;
  color: #616161;
  background-color: transparent;
  text-align: center;
  font-size: 26px;
  padding: 0;
  margin-left: 1rem;
  margin-right: 1rem;
`;

class ConfirmationInput extends React.Component {
  inputRefs = [];

  constructor(props) {
    super(props);
    this.state = {
      inputs: new Array(this.props.count).fill(""),
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

    inputs[index] = value;

    if (count > index + 1) {
      this._setFocus(index + 1);
    } else if (onFinished) {
      const current = inputs.reduce((x, y) => x + y, new String());
      onFinished(current);
    }

    this.setState(state => ({
      inputs: [...inputs],
      index: state.index + 1
    }));
  };

  _setFocus = index => {
    this.inputRefs[index].focus();
  };

  onFocused = index => {
    const { inputs } = this.state;
    const emptyIndex = inputs.findIndex(e => !e);

    if (emptyIndex !== -1 && emptyIndex < index) {
      this._setFocus(emptyIndex);
      return;
    }

    if (inputs[index]) {
      for (const i in inputs) {
        if (i >= index) {
          inputs[i] = "";
        }
      }

      this.setState({
        index: index,
        inputs: [...inputs]
      });
    }
  };

  onKeyDown = event => {
    if (event.nativeEvent.key === "Backspace") {
      const { index, inputs } = this.state;
      const nextIndex = index > 0 ? index - 1 : 0;
      inputs[nextIndex] = null;
      this._setFocus(nextIndex);
      this.setState({
        inputs: [...inputs],
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
            autoFocus={index === key}
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

export default ConfirmationInput;
