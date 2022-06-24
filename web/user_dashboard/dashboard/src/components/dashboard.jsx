import React from "react";
import navbarLogo from "./navbar-logo.png";

class Dashboard extends React.Component {
	render() {
		return (
			<div>
				<meta charSet="utf-8" />
				<meta
					name="viewport"
					content="width=device-width, initial-scale=1, shrink-to-fit=no"
				/>
				<link rel="shortcut icon" href="images/favicon.png" />
				<meta name="description" content />
				<meta name="author" content />
				<title>Gas Monitoring System</title>
				<link
					href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
					rel="stylesheet"
					integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
					crossOrigin="anonymous"
				/>
				<link
					href="https://fonts.googleapis.com/css?family=Muli:400,600,700,800,900|Quicksand:300,400,500,700"
					rel="stylesheet"
				/>
				<style
					dangerouslySetInnerHTML={{
						__html:
							'\n@import url("https://fonts.googleapis.com/css2?family=Cedarville+Cursive&family=Homemade+Apple&display=swap");\n    ',
					}}
				/>
				<link href="index.css" rel="stylesheet" />
				<div className="banner_inner">
					<canvas
						id="myChart"
						style={{ width: "100%", maxWidth: "700px" }}></canvas>
				</div>
				<div className="container">
					<nav className="navbar navbar-expand-lg navbar-light bg-light fixed-top">
						<div className="container-fluid">
							<img
								width="50px"
								height="45px"
								src={navbarLogo}
								alt="NavBar Logo"
							/>

							<div>
								<span
									style={{
										fontFamily: '"PT Sans Narrow", sans-serif',
										fontSize: "30px",
										color: "rgb(203, 140, 140)",
									}}>
									GAS CYLINDER INFORMATION
								</span>
							</div>
							<form className="d-flex">
								<button type="button" className="btn btn-outline-secondary">
									Book Now
								</button>
							</form>
						</div>
					</nav>
				</div>
				<div>
					<section className="Project-Abstract-div">
						<div className="container">
							<div className="div_visdetails">
								<div className="bottom-header">
									<h2>Cylinder Analytics</h2>
								</div>
								<div
									className="container"
									style={{
										display: "flex",
										backgroundColor: "rgb(249, 243, 236)",
										width: "100%",
									}}>
									<div className="column column-1">
										<h4>How We Do It</h4>
										<p>
											We're leveraging sensor technology to determine LPG gas
											usage as well as leakages in the cylinder. These values
											and changes in state are notified to the user on the
											website and through SMS. The user can thus take
											appropriate measures such as booking a new cylinder on the
											same website.
										</p>
									</div>
									<div className="column">
										<h4>Tips to Save Cooking Gas</h4>
										<ul>
											<div className="list-item">
												<li>
													<i className="fa fa-angle-double-right" />
													You can cook your dishes faster and use less gas at
													the same time by covering the pans with a lid.
												</li>
											</div>
											<div className="list-item">
												<li>
													<i className="fa fa-angle-double-right" />
													Go for ISI certified gas stoves as they are known to
													save up to 15% on your LPG and cook more efficiently.
												</li>
											</div>
											<div className="list-item">
												<li>
													<i className="fa fa-angle-double-right" />
													If the flame coming out from your burner looks orange,
													yellow, or not so uniform, then there’s probably some
													carbon deposit on it. Take a look and clean it up.
												</li>
											</div>
											<div className="list-item">
												<li>
													<i className="fa fa-angle-double-right" />
													Set aside both a small and a larger-sized burner for
													times when you want to cook quick or slow.
												</li>
											</div>
										</ul>
									</div>
								</div>
							</div>
						</div>
					</section>
				</div>
				<div>
					<nav className="navbar navbar-light bg-light">
						<div className="container-fluid">
							<div className="navbar-text width:100%;">
								©&nbsp;&nbsp;Gas Agency
							</div>
						</div>
					</nav>
				</div>
			</div>
		);
	}
}

export default Dashboard;
