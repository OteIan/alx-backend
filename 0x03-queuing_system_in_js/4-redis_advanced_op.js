#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

const client = createClient();
client.on('error', (error) => {
  console.log('Redis client not connected to the server: ' + error.toString());
});

function main () {
  const Obj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  for (const [field, value] of Object.entries(Obj)) {
    client.HSET('HolbertonSchools', field, value, print);
  }
  client.HGETALL('HolbertonSchools', (_err, reply) => {
    console.log(reply);
  });
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
