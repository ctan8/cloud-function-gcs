const { Storage } = require('@google-cloud/storage');
const storage = new Storage({ keyFilename: 'key.json' });

exports.copyFile = async (event, context) => {
  const file = storage.bucket(event.bucket).file(event.name);
  const destination = storage.bucket(event.bucket).file(`new_folder/${file.name}`);

  await file.copy(destination);

  console.log(`File ${file.name} copied to ${destination.name}.`);
};