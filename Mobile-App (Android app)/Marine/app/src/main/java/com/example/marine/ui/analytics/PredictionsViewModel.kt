package com.example.marine.ui.predictions

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableDoubleStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel

class PredictionsViewModel : ViewModel() {

    var predictedFuel by mutableDoubleStateOf(24.6)
    var failureRisk by mutableIntStateOf(12)
    var anomalyProbability by mutableIntStateOf(8)

}