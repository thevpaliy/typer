import React from "react";
import AnimationBuilder from "Components/Animation";
import styled from "styled-components";

const NotFoundPage = new AnimationBuilder(require("./404.json"))
  .withHeight(800)
  .withWidth(800)
  .withStyle({ marginTop: "1rem", padding: 0 })
  .withLoop(true)
  .withAutoplay(true)
  .build();

export default NotFoundPage;
