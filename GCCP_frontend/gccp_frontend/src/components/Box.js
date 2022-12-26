
import { Button, Grid} from '@mui/material';
import MoreVertIcon from '@mui/icons-material/MoreVert';

function Box() {
  return (
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
    <Button type="submit" color="primary" variant="text" sx={ { borderRadius: 50, color: '#fff'} }> 
    <MoreVertIcon/>
    </Button>
     </Grid>
     <Grid item xs={1}></Grid>
  </Grid></Box>
  );
}

export default Box;
