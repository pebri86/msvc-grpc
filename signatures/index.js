const { addSignaturePlaceholderToPdf, CertificationLevels, pdfDigest, signPdf, addLtvToPdf } = require('pdf-signatures');
const { HashAlgorithms } = require('pdf-signatures');

const jwToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InBlcnNvbmFsLnRlc3Quc3RnQHlvcG1haWwuY29tIiwic3ViIjoiNjI2MGUyMWMzYWM0NWIwMDM4YmU3YmFkIiwiYXVkIjoiaHR0cHM6Ly9lLW1ldGVyYWkuY28uaWQiLCJpc3MiOiJlbWV0ZXJhaSIsImp0aSI6IjQ1OTJkZGQzLTk1MzgtNGMyZC1hMmJlLTdiZjhjNDhhZmEyNSIsImV4cCI6MTcwMTAwMTEwOCwiaWF0IjoxNzAwOTE0NzA4fQ.jhM9oOqDJmCg4BsJkubgk5ouiiO8deKguJwCZcQoF7E"

const getExternalSignature = async (token, refToken, pdfDigest, shaChecksum) => {
    let headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Content-Type": "application/json"
    }

    let bodyContent = JSON.stringify({
        "profileName": "emeteraicertificateSigner",
        "data": pdfDigest,
        "shaChecksum": shaChecksum,
        "jwToken": token,
        "refToken": refToken
    });

    let response = await fetch("https://stampservicestg.e-meterai.co.id/keystampv2/pdfsigning/rest/docSigningM", {
        method: "POST",
        body: bodyContent,
        headers: headersList
    });

    let data = JSON.parse(await response.text());
    return data;
}

const run = async () => {
    var dt = new Date().getTime();

    await addSignaturePlaceholderToPdf({
        file: 'file.pdf',
        out: 'placeholdered.pdf',
        estimatedsize: 30000,
        certlevel: CertificationLevels.NotCertified,
        reason: 'I want to sign the document',
        location: 'Moon',
        contact: 'John Doe', // Signing contact, Optional, Default is undefined
    });

    const shaChecksum = await pdfDigest({
        file: 'file.pdf',                   // Path to file, Required
        algorithm: HashAlgorithms.Sha256,            // Hash algorithm, Optional, Default is HashAlgorithms.Sha512
    });

    const base64EncodedDigest = await pdfDigest({
        file: 'placeholdered.pdf',                   // Path to file, Required
        algorithm: HashAlgorithms.Sha256,            // Hash algorithm, Optional, Default is HashAlgorithms.Sha512
    });

    let data = await getExternalSignature(jwToken, "ACCTL6L1230GUAPI0001T9", base64EncodedDigest, shaChecksum)
    console.log(data)
    await signPdf({
        file: 'placeholdered.pdf',                   // Path to file, Required
        out: 'signed.pdf',                     // Output file path, Required
        signature: data.data,                       // Base64-encoded external signature
        password: ''
    });

    await addLtvToPdf({
        file: 'signed.pdf', // Path to file, Required
        out: 'signed-ltv.pdf',   // Output file path, Required
        crl: data.crlEntries,
        ocsp: data.ocspEntries,
    });

}

run()