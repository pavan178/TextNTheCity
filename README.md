# TextNTheCity

## Text and the City - Training
📚 This notebook demonstrates how to fine-tune a BERT-like model for multi-label classification using an Excel file containing the "Text and the City" data.

🔍 Note: This notebook does not cover the extraction of content from PDF files. For that, please refer to the other provided notebook.

🚀 The notebook was executed on a free instance of Google Colab with 12.7 GB RAM, but it can be readily adapted to a regular Jupyter Notebook that can be run in any suitable environment.

### Label Data
🏷️ Retain only the "Name des pdf Dokuments" and "Inhalt" (content) columns from the dataframe and eliminate duplicate entries. Create a new column for each document named "labels", containing an array. The array has a length equal to the number of unique goals. Set the value to 1 when the index corresponds to the goal associated with that document and 0 otherwise.

### Choose Model
🤖 Specify the name of a model available on Hugging Face.

Some options:

- microsoft/mdeberta-v3-base
- bert-base-multilingual-cased

Visit this link 👉 https://huggingface.co/models for additional models. You can filter for language German and task Classification to explore other models.

### Define Metrics
📏 This function defines the metrics used to evaluate the model and how these metrics are computed.

In this case, the f1 score, the ROC curve, and accuracy are computed. It is recommended to refer to the respective Wikipedia pages for more information on these metrics.

The overall metric used is the f1 score with micro average. For additional information and alternatives, refer 👉https://towardsdatascience.com/evaluating-multi-label-classifiers-a31be83da6ea 

The overall metric used can be changed; it has to be implemented in the multi_label_metrics function, and then the metric_for_best_model parameter in the cell above has to be set accordingly.

Keep in mind that the choice of the overall metric significantly influences how the model is trained.

### NOTE:

The threshold value determines how high a value after the last sigmoid function must be to consider it a relevant goal for the given input text. This value can be adjusted as needed.

### Final Remarks
🔍 The current number of labels is 25, resulting in 2<sup>25</sup> = 33,554,432 possible multi-label variations. Clustering the labels may be necessary.

📉 The dataset is showing signs of overfitting, with low f1-score and accuracy. Consider augmenting the dataset size, even if further reduction in the number of labels is implemented.

📊 Investigating the distribution of labels in the datapoints is crucial. Currently, it may not provide meaningful insights due to the imbalance between the numerous classes and limited datapoints. (histograms, confusion matrices)

🛠️ As previously mentioned, certain aspects can be modified to enhance the model, including the choice of the base model, adjustment of hyperparameters, refining tokenization methods (summarizing before, windowing), fine-tuning thresholds, and optimizing output layer functions.

## Text and the City - Text Extraction
🔍 This notebook demonstrates how to extract the "Inhalt" (content) from PDF files.

🚀 Note: This notebook does not cover how to fine-tune a BERT-like model for multi-label classification; for that, please refer to the other provided notebook.

📚 The notebook was executed on a free instance of Google Colab with 12.7 GB RAM, but it can be easily adapted to a regular Jupyter Notebook that can be run anywhere.

### Extract Data
📄 Extract the text from all PDF files and try to identify a "Begründung" section, starting with "Begründung" and ending with three empty spaces. If this section is not found, the file is skipped.

### NOTE:

This implementation is basic, and there is room for improvement. Consider exploring additional keywords or alternative methods for extracting the relevant section.
