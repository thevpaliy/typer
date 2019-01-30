import React from "react";
import Lottie from "react-lottie";

class AnimationBuilder {
  constructor(jsonFile) {
    this.jsonFile = jsonFile;
    this.isLoopEnabled = false;
    this.isAutoplayEnabled = false;
    this.rendererSettings = {};
    this.width = 50;
    this.height = 50;
    this.speed = null;
    this.style = { margin: 0 };
  }

  withLoop(enable) {
    this.isLoopEnabled = enable;
    return this;
  }

  withStyle(style) {
    this.style = style;
    return this;
  }

  withSpeed(speed) {
    this.speed = speed;
    return this;
  }

  withAutoplay(enable) {
    this.isAutoplayEnabled = enable;
    return this;
  }

  withRenderSettings(settings) {
    this.rendererSettings = settings;
    return this;
  }

  withHeight(height) {
    this.height = height;
    return this;
  }

  withWidth(width) {
    this.width = width;
    return this;
  }

  build() {
    const defaultOptions = {
      loop: this.isLoopEnabled,
      autoplay: this.isAutoplayEnabled,
      animationData: this.jsonFile,
      rendererSettings: this.rendererSettings
    };
    const config = {
      height: this.height,
      width: this.width,
      style: this.style,
      speed: this.speed,
      options: defaultOptions
    };
    return createAnimation(config);
  }
}

export const createAnimation = config =>
  class Animation extends React.Component {
    render() {
      return <Lottie {...config} />;
    }
  };

export default AnimationBuilder;
