import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Avatar from '@mui/material/Avatar';
import Stack from '@mui/material/Stack';
import { deepOrange, deepPurple } from '@mui/material/colors';

function createData(sln, photo, name, email, mobile, post) {
  return { sln, photo, name, email, mobile, post };
}

const rows = [
  createData(1, 'Photo', 'abc', 'abc@email.com', 1234567890, 'Club Coordinator'),
  createData(2, 'Photo', 'abc', 'abc@email.com', 1234567890, 'Club Coordinator'),
  createData(3, 'Photo', 'abc', 'abc@email.com', 1234567890, 'Club Coordinator'),
];

export default function BasicTable() {
  return (
    <TableContainer component={Paper} sx={{ borderRadius: '16px' }}>
      <Table sx={{ minWidth: 650}} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell align="center">Sl No.</TableCell>
            <TableCell align="left">Photo&nbsp;</TableCell>
            <TableCell align="center">Name&nbsp;</TableCell>
            <TableCell align="center">Mobile&nbsp;</TableCell>
            <TableCell align="center">Email&nbsp;</TableCell>
            <TableCell align="center">Position&nbsp;</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row" align="center" sx={{fontWeight:"bold"}}>
                {row.sln}
              </TableCell>
              <TableCell sx={{fontWeight:"bold"}}><Avatar sx={{ bgcolor: deepPurple[500]}}>{row.name[0].toUpperCase()}</Avatar></TableCell>
              <TableCell align="center" sx={{fontWeight:"bold"}}>{row.name}</TableCell>
              <TableCell align="center" sx={{fontWeight:"bold"}}>{row.email}</TableCell>
              <TableCell align="center" sx={{fontWeight:"bold"}}>{row.mobile}</TableCell>
              <TableCell align="center" sx={{fontWeight:"bold"}}>{row.post}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}