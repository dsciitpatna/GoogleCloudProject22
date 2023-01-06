import '../css/createevent.css'
import * as React from 'react';
import { TextField } from '@mui/material';
import ResponsiveTimePickers from '../components/TimePicker';
import DatePickerValue from '../components/DatePicker';
import TagSelect from '../components/TagSelect'
import { Button } from '@mui/material';
import Sidebar from '../components/sidebar/index'
import Header from '../components/header/index'
import TypePicker from '../components/TypePicker'
import Box from '@mui/material/Box';
import Alert from '@mui/material/Alert';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
function CreateEvent() {
  const names = {
    'Quiz': 1,
    'Seminar': 2,
    'Workshop': 3,
    'Session': 4,
    'Talk': 5,
    'Fest': 6,
    'Others': 7,

  };
  const navigate = useNavigate();
  const [alertVisib, setAlertVisib] = useState(false);
  const displayAlert = () => {
    setAlertVisib(true);

    setTimeout(() => {
                setAlertVisib(false);
            }, 3000);
  }
  const HOST = process.env.REACT_APP_HOST
  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    var array = data.get('tags').split(",")
    var list1 = []
    for (let index = 0; index < array.length; index++) {
      list1.push(names[array[index]])

    }
    const mess = {
      "name": data.get('name-of-event'),
      "description": data.get('description'),
      "_type": data.get('type'),
      "tags": list1,
      "start_date": data.get('date') + "T" + data.get('start_time'),
      "end_date": data.get('date') + "T" + data.get('end_time'),
      "social_links": data.get('social_links'),
      "rsvp_link": data.get('rsvp_link')
    };
    console.log(mess);
    let response = await fetch(`${HOST}/events/create`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },

      body: JSON.stringify(mess),
    });



    console.log(response.data)
    if (response.status === 203) {
      navigate("/");
    }
    else if (response.status === 201) {
      displayAlert();

    }
    else {
      navigate("/signup");
    }



  };
  return (
    <div className="sidebar-mini skin-black-light">
  
      <Header />
      <Sidebar />
      <div className="content-wrapper">
        <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
        {
      alertVisib && <Alert severity="success" >
        <p style={{fontSize: 12}}>Event Created Successfully.</p>
      </Alert>
    }
          <div class="createevent content">
            <div class="createevent content">

              <div class="form-q">Event Name *</div>
              <TextField id="name-of-event" name="name-of-event"
                placeholder="Enter Name of the Event"
                sx={{ width: "100%" }}
                inputProps={{ style: { fontSize: 12 } }}
                InputLabelProps={{ style: { fontSize: 12 } }} />

              <div class="form-q">Description *</div>
              <TextField id="description" name="description"
                placeholder="Enter Description"
                multiline
                rows={4}
                sx={{ width: "100%" }}
                inputProps={{ style: { fontSize: 12 } }}
                InputLabelProps={{ style: { fontSize: 12 } }}
              />


              <div id="datetimewrapper">
                <div id="timewrapper">
                  <div class="form-q">Time *</div>
                  <div id="timepickerwrapper">
                    <div class="datetime">
                      <ResponsiveTimePickers id="start_time" label="Start Time" />
                    </div>
                    <div class="datetime">
                      <ResponsiveTimePickers id="end_time" label="End Time" />
                    </div>
                  </div>
                </div>
                <div id="datewrapper">
                  <div class="form-q">Date *</div>
                  <DatePickerValue label="date" />
                </div>
              </div>
              <div class="form-q">Tags *</div>

              <TagSelect />
              <div class="form-q">Types *</div>

              <TypePicker sx={{ width: "100%" }} />
              <div class="form-q">Social Media Link</div>
              <TextField id="social_links" name="social_links"
                placeholder="Enter Link of Social Media"
                sx={{ width: "100%" }}
                inputProps={{ style: { fontSize: 12 } }}
                InputLabelProps={{ style: { fontSize: 12 } }} />
              <div class="form-q">RSPV Link </div>
              <TextField id="rsvp_link" name="rsvp_link"
                placeholder="Enter RSPV Link"
                sx={{ width: "100%" }}
                inputProps={{ style: { fontSize: 12 } }}
                InputLabelProps={{ style: { fontSize: 12 } }} />
            </div>


            <Button
              type="submit"
              color="secondary"
              id="create-event-button"
              variant="contained"
              sx={{
                borderRadius: 50,
                textTransform: 'none',
                fontWeight: 'bold',
                fontSize: "15px",
                marginTop: 10
              }}
            >
              Create Event
            </Button>
          </div>
        </Box>
      </div>
    </div>

  );
}

export default CreateEvent;
