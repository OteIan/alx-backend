#!/usr/bin/yarn dev
import { createClient } from 'redis';

const client = createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

function main () {
  client.subscribe('holberton school channel');

  client.on('message', (_channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe();
      client.quit();
    }
  });
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
