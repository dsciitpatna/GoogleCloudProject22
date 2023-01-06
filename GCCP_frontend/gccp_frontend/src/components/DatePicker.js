import * as React from 'react';
import dayjs from 'dayjs';
import TextField from '@mui/material/TextField';
import Stack from '@mui/material/Stack';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';

export default function ResponsiveDatePickers(props) {
  const [value, setValue] = React.useState(dayjs('2022-04-07'));

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <Stack spacing={3}>
        
        <DatePicker
          openTo="year"
          views={['year', 'month', 'day']}
          value={value}
          inputFormat="YYYY-MM-DD"
          inputProps={{ style: { fontSize: 12 } }}
            InputLabelProps={{ style: { fontSize: 12 } }} 
          onChange={(newValue) => {
            setValue(newValue);
            
          }}
          renderInput={(params) => <TextField {...params} id={props.label} name={props.label}/>}
        />
      </Stack>
    </LocalizationProvider>
  );
}
