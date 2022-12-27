import Navbar from '../components/Navbar'
import '../css/addmember.css'
import * as React from 'react';
import { TextField } from '@mui/material';
import PositionSelect from '../components/PositionSelect'
import { Button} from '@mui/material';

function AddMember() {
  return (
    <div>
      <Navbar />
      <div class="addmember">

        <div class="form-q">Name *</div>
        <TextField id="name-of-member"
          placeholder="Member Name"
          sx={{ width: "100%" }} />
        
        <div class="form-q">Email *</div>
        <TextField id="email-of-member"
          placeholder="Enter the email"
          sx={{ width: "100%" }} />

        <div class="form-q">Positions held *</div>

        <PositionSelect/>
        <Button 
          type="submit" 
          color="secondary" 
          id="add-member-button" 
          variant="contained" 
          sx={ { borderRadius: 50,
          textTransform: 'none', 
          fontWeight:'bold', 
          marginTop:10 } }>
            Add Member
            </Button>
      </div>
    </div>
  );
}

export default AddMember;
