import React from 'react';
import type {AppProps} from 'next/app'
import {ThemeProvider, createTheme} from '@mui/material/styles';
import { Box, Container} from "@mui/material";
import CssBaseline from '@mui/material/CssBaseline';
import {Navbar} from "../components";


const darkTheme = createTheme({
	palette: {
		mode: 'dark',
	},
});

function MyApp({Component, pageProps}: AppProps) {
	return (
		<ThemeProvider theme={darkTheme}>
			<CssBaseline/>
			<Navbar/>
			<Container maxWidth="md">
				<Box
					mt={10}
				>
					<Component {...pageProps} />
				</Box>
			</Container>
		</ThemeProvider>
	)
}

export default MyApp
