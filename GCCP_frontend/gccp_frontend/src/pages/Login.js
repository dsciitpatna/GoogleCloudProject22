import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import GitHubIcon from '@mui/icons-material/GitHub';
import GoogleIcon from '@mui/icons-material/Google';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useNavigate } from 'react-router-dom';

const theme = createTheme();
const HOST = process.env.REACT_APP_HOST;

export default function LogIn() {
  const navigate = useNavigate();
  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const body = {
      email: data.get("email"),
      password: data.get("password"),
    };
    let response = await fetch(`${HOST}/user/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify(body),
    });
    
    let result = await response.json();
    console.log(result);
  };

  const handleGOauth = (event) => {
    // bind a link for google oauth
    event.preventDefault();
    const location = "http://127.0.0.1:8000/accounts/google/login/";
    window.location = location;
  }

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Log In
          </Typography>
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              autoComplete="email"
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
            />
            <h6>OR</h6>
            <Grid container>
              <Grid xs={6}>
              <Button variant="outlined" color='secondary'><GitHubIcon/> &ensp; GitHub</Button>
              </Grid>
              <Grid xs={6}>
              <Button variant="outlined" color='secondary' onClick={handleGOauth}><GoogleIcon/> &ensp; Google</Button>
              </Grid>
            </Grid>

            <Button
              type="submit"
              fullWidth
              variant="contained"
              color='secondary'
              sx={{ mt: 3, mb: 2 }}
            >
              Log In
            </Button>
            <Grid container>
              <Grid item xs>
                <Link href="#" variant="body2">
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link href="/signup" variant="body2">
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
        
      </Container>
    </ThemeProvider>
  );
}