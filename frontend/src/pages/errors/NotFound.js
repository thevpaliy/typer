import React from "react";
import AnimationBuilder from "Components/Animation";
import styled from "styled-components";

const NotFoundAnimation = new AnimationBuilder(require("./404.json"))
  .withHeight(800)
  .withWidth(800)
  .withStyle({ marginTop: "1rem" })
  .withLoop(false)
  .withAutoplay(true)
  .build();


const NotFoundPage = () => (
  <div>
    <h1>Not Found</h1>
    <p>You just hit a route that doesn&#39;t exist... the sadness.</p>
  </div>
);

export default NotFoundAnimation;
