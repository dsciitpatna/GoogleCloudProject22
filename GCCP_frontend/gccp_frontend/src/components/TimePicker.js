import * as React from 'react';
import dayjs from 'dayjs';
import TextField from '@mui/material/TextField';
import Stack from '@mui/material/Stack';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { MobileTimePicker } from '@mui/x-date-pickers/MobileTimePicker';

export default function ResponsiveTimePickers(props) {
  const [value, setValue] = React.useState(dayjs('2018-01-01T00:00:00.000Z'));

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <Stack spacing={3}>
        <MobileTimePicker
          label={props.label}
          value={value}
          onChange={(newValue) => {
            setValue(newValue);
          }}
          renderInput={(params) => <TextField {...params} />}
        />
        
      </Stack>
    </LocalizationProvider>
  );
}