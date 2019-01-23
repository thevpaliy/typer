import React from "react";
import styled from "styled-components";
import NavLink from "./NavLink";

const LinkWrapper = styled.div`
  background-color: #f6f6f6;
  border-top: 1px solid #dce8f1;
  padding: 25px;
  margin-top: 25px;
  text-align: center;
  -webkit-border-radius: 0 0 10px 10px;
  border-radius: 0 0 10px 10px;
`;

const AuthFooter = ({ path, text }) => (
  <LinkWrapper>
    <NavLink path={path} text={text} />
  </LinkWrapper>
);

export default AuthFooter;
