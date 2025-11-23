const qrDirective = {
  name: 'qr',
  doc: 'Generate a QR code image for a given URL or text.',
  arg: {
    type: String,
    doc: 'The content to encode in the QR code.',
    required: true
  },
  options: {
    size: { type: String, doc: 'Size of the image in pixels (e.g. 150). Default is 150.' },
    color: { type: String, doc: 'Color of the QR code (hex, e.g. 000000). Default is 000000.' },
  },
  run(data) {
    const content = encodeURIComponent(data.arg);
    const size = data.options?.size || '150';
    const color = data.options?.color || '000000';
    
    const url = `https://api.qrserver.com/v1/create-qr-code/?size=${size}x${size}&data=${content}&color=${color}`;
    
    return [{
      type: 'image',
      url: url,
      alt: `QR Code for ${data.arg}`,
      title: `QR Code: ${data.arg}`
    }];
  },
};

const plugin = { name: 'QR Code Generator', directives: [qrDirective] };

export default plugin;
