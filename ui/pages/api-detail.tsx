import {SetStateAction, useState} from "react";
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import {Box, Typography} from "@mui/material";
const a11yProps = (index: number) => {
	return {
		id: `simple-tab-${index}`,
		'aria-controls': `simple-tabpanel-${index}`,
	};
}
// @ts-ignore
const TabPanel = (props) => {
	const { children, value, index, ...other } = props;

	return (
		<div
			role="tabpanel"
			hidden={value !== index}
			id={`simple-tabpanel-${index}`}
			aria-labelledby={`simple-tab-${index}`}
			{...other}
		>
			{value === index && (
				<Box sx={{ p: 3 }}>
					<Typography>{children}</Typography>
				</Box>
			)}
		</div>
	);
}


const ApiDetail = () => {

	const [value, setValue] = useState(0);

	const handleChange = (event: any, newValue: SetStateAction<number>) => {
		setValue(newValue);
	};

	return (
		<div>
			<Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
				<Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
					<Tab label="Lista cenzopap" {...a11yProps(0)} />
					<Tab label="Losowe cenzo" {...a11yProps(1)} />
				</Tabs>
			</Box>
			<TabPanel value={value} index={0}>
				<Typography variant={"h3"}>
					Lista cenzo
				</Typography>
				<Typography variant={"h6"}>
					Aby pobrac liste cenzo nalezy wyslac zapytanie na adres https://api.jebzpapy.tk
				</Typography>
				<Typography variant={"h6"}>
					10 ostatnich cenzo - <code>https://api.jebzpapy.tk/images</code>
				</Typography>
			</TabPanel>
			<TabPanel value={value} index={1}>
				Item Two
			</TabPanel>
		</div>

	)
}

export default ApiDetail