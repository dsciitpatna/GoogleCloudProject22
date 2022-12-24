import { drawerClasses } from '@mui/material';
import Navbar from '../components/Navbar'
import '../css/createevent.css'
import * as React from 'react';
import { OutlinedInput, TextField } from '@mui/material';
import FormControl from '@mui/material/FormControl';
import ResponsiveTimePickers from '../components/TimePicker';
import DatePickerValue from '../components/DatePicker';
import TagSelect from '../components/TagSelect'
import { Button} from '@mui/material';

const drawerWidth = 240;

function CreateEvent() {
  return (
    <div>
      <Navbar />
      <div class="createevent">

        <div class="form-q">Event Name *</div>
        <TextField id="name-of-event"
          placeholder="Enter Name of the Event"
          sx={{ width: "100%" }} />

        <div class="form-q">Description *</div>
        <TextField
          placeholder="Enter Description"
          multiline
          rows={4}
          sx={{ width: "100%" }}
        />

        <div class="form-q">Location *</div>
        <TextField id="name-of-event"
          placeholder="Location"
          sx={{ width: "100%" }} />

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

        <TagSelect/>
        <Button 
          type="submit" 
          color="secondary" 
          id="create-event-button" 
          variant="contained" 
          sx={ { borderRadius: 50,
          textTransform: 'none', 
          fontWeight:'bold', 
          marginTop:10 } }>
            Create Event
            </Button>
      </div>
    </div>
  );
}

export default CreateEvent;
