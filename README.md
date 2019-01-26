# covariance_diagnostic

A tool to return some useful information about a covariance matrix. When encountering a covariance matrix there are some properties that are not immediately apparent. This includes whether it is positive definite, what the eigenvalues are, and how many degrees of freedom it has.

This small tool computes all of those things and presents them in a useful way.

## Usage

```python
import covariance_diagnostic

#Assume a covariance matrix C came from somewhere
C = ...

diagnostic = covariance_diagnostic.covdiagnostic(C)

print(diagnostic) #To see all properties
```