#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const queue = createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '0758698453',
  message: 'Line Registered'
});

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('error', (_error) => {
  console.log('Notification job failed');
});

job.save();
