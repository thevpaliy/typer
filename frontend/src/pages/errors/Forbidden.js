import React from "react";
import AnimationBuilder from "Components/Animation";
import styled from "styled-components";

const WarningAnimation = new AnimationBuilder(require("./warning.json"))
  .withHeight(600)
  .withWidth(600)
  .withStyle({ marginTop: "1rem" })
  .withLoop(false)
  .withAutoplay(true)
  .build();

const ForbiddenPage = () => <WarningAnimation />;

export default ForbiddenPage;
