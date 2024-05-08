#!/usr/bin/yarn dev

export default function createPushNotificationsJobs (jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error('Job is not an array');
  }

  for (const job of jobs) {
    const newJob = queue.create('push_notification_code_3', job);

    newJob
      .on('enqueue', () => {
        console.log('Notification job created:', newJob.id);
      })
      .on('complete', () => {
        console.log(`Notification job ${newJob.id} completed`);
      })
      .on('failed', (error) => {
        console.log(`Notification job ${newJob.id} failed: ${error.toString()}`);
      })
      .on('progress', (progress, _data) => {
        console.log(`Notification job #${newJob.id} ${progress}% complete`);
      });
    newJob.save();
  }
}
