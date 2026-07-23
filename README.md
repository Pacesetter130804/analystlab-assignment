# AnalystLab Production Prediction API 🚀

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-F7931E.svg)

A lightweight RESTful API designed to serve real-time machine learning predictions using **FastAPI**, **Scikit-Learn**, and **Uvicorn**.

---

## 📌 Project Overview

This project transitions a trained Machine Learning classification model from an experimental notebook environment into a production-ready API service. The endpoint accepts feature vectors via JSON requests and returns real-time class predictions.

### Key Features
* **Model Serialization:** Uses `joblib` for efficient loading of serialized ML pipelines.
* **Schema Validation:** Leverages **Pydantic** models to validate incoming request payloads.
* **Auto-Generated Docs:** Interactive OpenAPI / Swagger UI served automatically at `/docs`.

---

## 📁 Repository Structure

```text
analystlab-deployment/
├── app/
│   └── main.py          # FastAPI application server & routes
├── model/
│   └── model.joblib     # Serialized machine learning model
├── week7.ipynb          # Model training notebook
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
