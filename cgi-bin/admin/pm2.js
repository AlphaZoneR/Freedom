var fs = require('mz/fs'); 
var exec = require('child_process').exec

exec('../venv/bin/python server.py', (error, stdout, stderr) => {
  if (error || stderr) {
    console.log(error + ' ' + stderr);
  }
  console.log('Starting new process...!')
  console.log('Started...')
})

setTimeout(async function worker() {
  console.log('Restarting...')
  const pid = await fs.readFile('pid')
  await exec('kill ' + pid, async (error, stdout, sterr) => {
    console.log('Previous stopped!')
    await exec('../venv/bin/python server.py', async (error, stdout, stderr) => {
      console.log('Starting new process...!')
      console.log('Restarted...')
    })
  })
  setTimeout(worker, 3600000);
}, 3600000);