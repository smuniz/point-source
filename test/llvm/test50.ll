; ModuleID = '../src/test50.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test50(i32 %value1) #0 {
  %1 = alloca i32, align 4
  %local1 = alloca i32, align 4
  store i32 %value1, i32* %1, align 4
  store i32 0, i32* %local1, align 4
  %2 = load i32, i32* %1, align 4
  %3 = icmp sgt i32 %2, 5
  br i1 %3, label %4, label %5

; <label>:4                                       ; preds = %0
  store i32 10, i32* %local1, align 4
  br label %5

; <label>:5                                       ; preds = %4, %0
  %6 = load i32, i32* %local1, align 4
  ret i32 %6
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
