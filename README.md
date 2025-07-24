# Face Recognition App with FastAPI + Docker (w600k\_r50.onnx)

A simple facial recognition system using FastAPI and FaceNet. Easily deployable with Docker.

---

## Features

* Upload and store face embeddings
* Real-time face recognition
* Delete face data
* RESTful API using FastAPI
* ONNX runtime with `w600k_r50.onnx`
* Dockerized for easy deployment

---

## Requirements

* Docker

---

## Endpoints

* `GET /api/face`
  Get a list of all faces in the database.

* `POST /api/face/register`
  Register a new face by adding its facial features to the database.

* `POST /api/face/recognize`
  Recognize a face by matching its facial features against the database and returning the matched face if found.

* `DELETE /api/face/{id}`
  Delete a face from the database by its ID.

---

## How to Run (Demo/Testing)

1. Open VS Code or WSL Ubuntu Terminal with Docker installed.
2. Pull the Docker image:

   ```bash
   docker pull evgb123/face-recog-test-app:latest
   ```
3. Run the Docker container:

   ```bash
   docker run -p 8000:8000 evgb123/face-recog-test-app
   ```
4. Open your browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to access the FastAPI Swagger UI.
5. To register a face:

   * Click on the `/api/face/register` section.
   * Click the "Try it out" button.
   * Upload your image and click "Execute".
6. To recognize a face:

   * Click on the `/api/face/recognize` section.
   * Click the "Try it out" button.
   * Upload your image and click "Execute".
7. To get a list of all registered faces:

   * Click on the `/api/face` section and click "Try it out" > "Execute".
8. To delete a face:

   * Click on the `/api/face/{id}` section.
   * Click the "Try it out" button.
   * Input the face ID from step 7 and click "Execute".

---

---

## Notes

To ensure accurate and reliable face recognition results, please follow these image guidelines:

- ✅ Use a **clear, front-facing image** of the person's face.
- ✅ Ensure the **face is centered** in the image and fully visible.
- ✅ Use **good lighting** (avoid shadows or overexposure).
- ✅ Upload images with **moderate distance** — not too close, not too far.
- ✅ Only **one face per image** is recommended.

Avoid:

- ❌ Blurry or low-resolution images
- ❌ Faces with sunglasses, heavy makeup, or masks
- ❌ Side profiles or extreme angles
- ❌ Group photos with multiple faces

Following these suggestions will help the model generate better embeddings and improve recognition accuracy.

