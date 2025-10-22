---
title: "Evaluate OCR Output Quality with Character Error Rate (CER) and Word Error Rate (WER)"
Link to the project: https://towardsdatascience.com/evaluating-ocr-output-quality-with-character-error-rate-cer-and-word-error-rate-wer-853175297510/ 
excerpt_separator: "<!--more-->"
categories:
  - project1
tags:
  - CER
  - WER
image: images/banner_PIC.jpg
---

Evaluate OCR Output Quality with Character Error Rate (CER) and Word Error Rate (WER)!

<!--more-->

Reading Kenneth Leung's blog gave me a deeper understanding of two key metrics used to evaluate OCR performance: **Character Error Rate (CER)** and **Word Error Rate (WER)**.  

Traditionally, we measure prediction accuracy by marking matches as **1** and mismatches as **0**. While this approach works for simple cases, it’s not enough to fully assess OCR performance. Error rates provide a clearer picture of how accurately text is being transcribed.  

## Types of OCR Errors

When evaluating OCR output, there are three main types of errors to watch for:

* **Substitution error** – replacing one character with another  
* **Deletion error** – removing a character  
* **Insertion error** – adding a character  

Understanding these errors is crucial for calculating more meaningful metrics.

## Levenshtein Distance

To quantify these errors, we use the **Levenshtein distance**. This metric measures the “distance” between two pieces of text by counting the minimum number of edits—insertions, deletions, or substitutions—needed to turn one word or sentence into another.  

In other words, the smaller the Levenshtein distance, the closer the OCR output is to the ground truth.

## Character Error Rate (CER)

**CER** uses the Levenshtein distance to measure OCR accuracy at the **character level**. It calculates the minimum number of character-level operations required to transform the reference (ground truth) text into the OCR output.

**CER formula:**

- **S** = Number of substitutions  
- **D** = Number of deletions  
- **I** = Number of insertions  
- **N** = Number of characters in the reference text  

CER is particularly useful when you care about exact character accuracy, such as in scanned documents, receipts, or forms.

## Word Error Rate (WER)

**WER** is more appropriate when working with full sentences or paragraphs where the meaning of words matters. It counts the number of word-level changes—substitutions, deletions, or insertions—needed to match the reference text.  

The formula for WER is the same as CER, but **W** represents word-level operations instead of characters.

WER usually correlates well with CER when error rates are moderate, though its absolute value is typically higher. This makes sense because even a single character error can cause a whole word to be counted as wrong.

---

Using both **CER** and **WER** together gives you a more complete picture of OCR performance, helping you understand both fine-grained character errors and higher-level word errors.  

