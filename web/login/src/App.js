import "./App.scss";
import React, { Component } from "react";
import LoginComponent from "./components/LoginComponent";
import "bootstrap/dist/css/bootstrap.min.css";
// import NavBar from "./components/NavBar";
class App extends Component {
	render() {
		return (
			<React.Fragment>
				{" "}
				{/* <NavBar /> */} <LoginComponent />
			</React.Fragment>
		);
	}
}

export default App;
