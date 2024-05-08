#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const queue = createQueue();
const BLACKLIST = [
  '4153518780',
  '4153518781'
];

function sendNotification (phoneNumber, message, job, done) {
  const total = 2;
  let waiting = 2;
  const interval = setInterval(() => {
    if (total - waiting <= total / 2) {
      job.progress(total - waiting, total);
    }
    if (BLACKLIST.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(interval);
      return;
    }
    if (total === waiting) {
      console.log(`Sending notification to ${phoneNumber} with message ${message}`);
    }
    --waiting || done();
    waiting || clearInterval(interval);
  }, 1000);
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
