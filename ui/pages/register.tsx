import {Avatar, Box, Button, Grid, Link, TextField, Typography} from "@mui/material";
import {useState} from "react";
import axios from "axios";

const Register = () => {
	const [username, setUsername] = useState('');
	const [password, setPassword] = useState('');
	const [email, setEmail] = useState('');

	const handleSubmit = (e: any) => {
		e.preventDefault();
		console.log(e);
		try {
			const url = process.env.NEXT_PUBLIC_API_URL
			const response = axios.post(`${url}/users/`, {
				email: email,
				username: username,
				password: password
			})
			console.log(response.data);
		} catch(e) {
			if (e.response) {
				console.log(e.re )
			}
			console.log(e);
		}

	}

	return (
		<Box
			sx={{
				marginTop: 8,
				display: 'flex',
				flexDirection: 'column',
				alignItems: 'center',
			}}
		>
			<Avatar sx={{ m: 1, bgcolor: 'secondary' }}>

			</Avatar>
			<Typography component="h1" variant="h5">
				Register
			</Typography>
			<Box component="form" method="post" onSubmit={handleSubmit} sx={{ mt: 1 }}>
				<TextField
					margin="normal"
					required
					fullWidth
					id="email"
					label="Email Address"
					name="email"
					type={"email"}
					autoComplete="email"
					autoFocus
					onChange={(e) => setEmail(e.target.value)}
					value={email}
				/>
				<TextField
					margin="normal"
					required
					fullWidth
					id="username"
					label="Username"
					name="username"
					autoComplete="username"
					onChange={(e) => setUsername(e.target.value)}
					value={username}
				/>
				<TextField
					margin="normal"
					required
					fullWidth
					name="password"
					label="Password"
					type="password"
					id="password"
					autoComplete="current-password"
					onChange={(e) => setPassword(e.target.value)}
					value={password}
				/>
				<Button
					type="submit"
					fullWidth
					variant="contained"
					sx={{ mt: 3, mb: 2 }}
				>
					Sign In
				</Button>
				<Grid container>
					<Grid item>
						<Link href="#" variant="body2">
							{"Don't have an account? Sign Up"}
						</Link>
					</Grid>
				</Grid>
			</Box>
		</Box>
	)
}

export default Register;