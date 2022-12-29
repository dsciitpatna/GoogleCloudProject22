import '../css/addmember.css'
import * as React from 'react';
import Sidebar from '../components/sidebar/index'
import Header from '../components/header/index'
import { TextField } from '@mui/material';
import '../css/profile.css'
function Profile() {
    return (
        <div className="sidebar-mini skin-black-light">
            <Header />
            <Sidebar />
            <div className="content-wrapper">
                <div class="content">


                    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet" />
                    <div class="container profile-page">
                        <div class="row">
                            <div class="col-xl-6 col-lg-7 col-md-12">
                                <div class="card profile-header">
                                    <div class="body">
                                        <div class="row">
                                            <div class="col-lg-4 col-md-4 col-12">
                                                <div class="profile-image float-md-right"> <img src="https://bootdey.com/img/Content/avatar/avatar7.png" alt="" /> </div>
                                            </div>
                                            <div class="col-lg-8 col-md-8 col-12">
                                                <TextField id="name-of-member"
                                                    defaultValue="Name Surname"
                                                    label="Name"
                                                    InputProps={{
                                                        readOnly: true,
                                                        style: { fontSize: 15 }
                                                    }}
                                                    sx={{ width: "100%", mt:3 }}
                                                    InputLabelProps={{ style: { fontSize: 12 } }} />

                                                <TextField id="email-of-member"
                                                    defaultValue="Email@email.com"
                                                    label="Email"
                                                    InputProps={{
                                                        readOnly: true,
                                                        style: { fontSize: 15 }
                                                    }}
                                                    sx={{ width: "100%", mt:3 }}
                                                    InputLabelProps={{ style: { fontSize: 12 } }} />

                                                <TextField id="Mobile-of-member"
                                                    defaultValue="1234567890"
                                                    label="Mobile No."
                                                    InputProps={{
                                                        readOnly: true,
                                                        style: { fontSize: 15 }
                                                    }}
                                                    sx={{ width: "100%", mt:3 }}
                                                    InputLabelProps={{ style: { fontSize: 12 } }} />

                                                <TextField id="position-of-member"
                                                    defaultValue="Club Coordinator"
                                                    label="Position"
                                                    InputProps={{
                                                        readOnly: true,
                                                        style: { fontSize: 15 }
                                                    }}
                                                    sx={{ width: "100%", mt:3 }}
                                                    InputLabelProps={{ style: { fontSize: 12 } }} />

                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>


                        </div>
                    </div>

                </div>
            </div>
        </div>

    );
}

export default Profile;
