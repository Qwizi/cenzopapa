import React from 'react';
import type {AppProps} from 'next/app'
import {ThemeProvider, createTheme} from '@mui/material/styles';
import { Box, Container} from "@mui/material";
import CssBaseline from '@mui/material/CssBaseline';
import {Navbar} from "../components";
import Head from 'next/head'

const darkTheme = createTheme({
	palette: {
		mode: 'dark',
	},
});

function MyApp({Component, pageProps}: AppProps) {
	return (
		<ThemeProvider theme={darkTheme}>
			<CssBaseline/>
			<Head>
				<title>Jebzpapy.tk</title>
			</Head>
			<Navbar/>
			<Container fixed>
				<Box
					mt={10}
					style={{ alignItems: "center", justifyContent: "center"}}
				>
					<Component {...pageProps} />
				</Box>
				<Box mt={10}
					 style={{ alignItems: "center", justifyContent: "center", textAlign: "center"}}
				>
					<p>Autor <a href={"https://github.com/Qwizi"}>Qwizi</a></p>
				</Box>
			</Container>
		</ThemeProvider>
	)
}

export default MyApp
