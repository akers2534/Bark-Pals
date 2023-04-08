import TinderCard from "react-tinder-card";
import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";

function Tinder() {
  const onSwipe = (direction) => {
    console.log("You swiped: " + direction);
  };

  const onCardLeftScreen = (myIdentifier) => {
    console.log(myIdentifier + " left the screen");
  };

  return (
    <TinderCard
      onSwipe={onSwipe}
      onCardLeftScreen={() => onCardLeftScreen("fooBar")}
      preventSwipe={["right", "left"]}
    >
      Hello, World!
    </TinderCard>
  );
}
export { Tinder };
