
from fastapi import FastAPI, UploadFile, File, HTTPException
from pypdf import PdfReader

app = FastAPI(title="Bookify API")


@app.get("/")
def home():
    return {
        "app": "Bookify",
        "message": "Your knowledge journey starts here.",
    }


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File (...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Atleast add pdfs man, cant work on other files, this is the only thing i can work on rn")
    contents = await file.read()
    if not contents.startswith(b"%PDF-"):
        raise HTTPException( status_code=400, detail = "Your pdf is invalid or it sucks, upload good stuff")

    from io import BytesIO
    pdf=PdfReader(BytesIO(contents))
    text = "\n".join(page.extract_text() or '' for page in pdf.pages)
    return {'filename': file.filename, 'text': text, 'pages': len(pdf.pages)}
