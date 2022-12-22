import './App.css';

import { Box, Button, Grid} from '@mui/material';
import { createTheme } from '@mui/material/styles';
import AddIcon from '@mui/icons-material/Add';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import Navbar from './components/Navbar'
const theme = createTheme({   
  palette: {
    primary: {
      light: '#757ce8',
      main: '#3f50b5',
      dark: '#002884',
      contrastText: '#fff',
    },
    secondary: {
      light: '#ff7961',
      main: '#f44336',
      dark: '#ba000d',
      contrastText: '#000',
    },
    white: '#fff',
  },   
  typography: {
    button: {
      textTransform: 'none',
      fontWeight:'bold',
    },
    
  }
}); 


function App() {
  return (
    <div className="App">
      {/* <Navbar/> */}
      <header className="App-header">
        
        Hello
        <Button type="submit" color="primary" variant="contained" sx={ { borderRadius: 50 } } theme={theme}> <AddIcon/> Add</Button>
        <Box
      sx={{
        width: 600,
        height: 35,
        borderRadius: 50,
        textAlign:"left",
        padding:1,
        display:'flex',
        color:'white',
        flexDirection:'row',
        alignContent:'center',
        backgroundColor: 'primary.main',
        '&:hover': {
          backgroundColor: 'primary.dark',
          opacity: [0.9, 0.8, 0.7],
        },
      }}
    ><Grid container spacing={2}>
      <Grid item xs={1}></Grid>
    <Grid item xs={9}>
      xs=8
    </Grid>
    <Grid item xs={1}>
    <Button type="submit" color="primary" variant="text" sx={ { borderRadius: 50, color: '#fff'} } theme={theme}> 
    <MoreVertIcon/>
    </Button>
     </Grid>
     <Grid item xs={1}></Grid>
  </Grid></Box>
  

      </header>
    </div>
  );
}

export default App;
