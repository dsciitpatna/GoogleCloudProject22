import '../css/addmember.css'
import * as React from 'react';
import { TextField } from '@mui/material';
import PositionSelect from '../components/PositionSelect'
import { Button } from '@mui/material';
import Sidebar from '../components/sidebar/index'
import Header from '../components/header/index'

function AddMember() {
  return (
    <div className="sidebar-mini skin-black-light">
      <Header />
      <Sidebar />
      <div className="content-wrapper">
        <div class="addmember content">

          <div class="form-q">Name *</div>
          <TextField id="name-of-member"
            placeholder="Member Name"
            sx={{ width: "100%" }} />

          <div class="form-q">Email *</div>
          <TextField id="email-of-member"
            placeholder="Enter the email"
            sx={{ width: "100%" }} />

          <div class="form-q">Positions held *</div>

          <PositionSelect />
          <Button
            type="submit"
            color="secondary"
            id="add-member-button"
            variant="contained"
            sx={{
              borderRadius: 50,
              textTransform: 'none',
              fontWeight: 'bold',
              fontSize: "15px",
              marginTop: 10
            }}>
            Add Member
          </Button>
        </div>
      </div>
    </div>
  );
}

export default AddMember;
