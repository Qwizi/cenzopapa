import {AppBar, Button, Container, Toolbar} from "@mui/material";
import Link from "next/link";
import Image from "next/image";
import Logo from "../public/logo.png";
import React from "react";

const Navbar = () => {
	return (
		<AppBar position="static" elevation={1}>
			<Toolbar>
				<Link href={"/"} passHref>
					<Image src={Logo} alt={"Jebzpapy"} width={150} height={50}/>
				</Link>
				<Container maxWidth="md">
					<Link href={"/random"} passHref>
						<Button>Wylosuj cenzo</Button>
					</Link>
					<Link href={"/api"} passHref>
						<Button>API</Button>
					</Link>
				</Container>
			</Toolbar>
		</AppBar>
	)
}

export default Navbar;