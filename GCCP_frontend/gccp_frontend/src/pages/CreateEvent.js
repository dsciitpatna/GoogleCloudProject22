import '../css/createevent.css'
import * as React from 'react';
import { TextField } from '@mui/material';
import ResponsiveTimePickers from '../components/TimePicker';
import DatePickerValue from '../components/DatePicker';
import TagSelect from '../components/TagSelect'
import { Button } from '@mui/material';
import Sidebar from '../components/sidebar/index'
import Header from '../components/header/index'

function CreateEvent() {
  return (
    <div className="sidebar-mini skin-black-light">
      <Header />
      <Sidebar />
      <div className="content-wrapper">

        <div class="createevent content">

          <div class="form-q">Event Name *</div>
          <TextField id="name-of-event"
            placeholder="Enter Name of the Event"
            sx={{ width: "100%" }}
            inputProps={{ style: { fontSize: 12 } }}
            InputLabelProps={{ style: { fontSize: 12 } }} />

          <div class="form-q">Description *</div>
          <TextField
            placeholder="Enter Description"
            multiline
            rows={4}
            sx={{ width: "100%" }}
            inputProps={{ style: { fontSize: 12 } }}
            InputLabelProps={{ style: { fontSize: 12 } }} 
          />

          <div class="form-q">Location *</div>
          <TextField id="name-of-event"
            placeholder="Location"
            sx={{ width: "100%" }} 
            inputProps={{ style: { fontSize: 12 } }}
            InputLabelProps={{ style: { fontSize: 12 } }} />

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
              <DatePickerValue />
            </div>
          </div>

          <div class="form-q">Tags *</div>

          <TagSelect />
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
            }}>
            Create Event
          </Button>
        </div>
      </div>
    </div>

  );
}

export default CreateEvent;
